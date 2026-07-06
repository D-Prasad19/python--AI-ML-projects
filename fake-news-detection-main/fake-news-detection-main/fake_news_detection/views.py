import joblib
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.feature_extraction.text import TfidfVectorizer

from fake_news_detection.models import NewsArticle
from fake_news_detection.forms import NewsArticleForm

# Load the modernized models
tfidf_vectorizer = joblib.load('vectorizer.sav')
pac = joblib.load('model.sav')


def base(request):
    return render(request, 'base.html')


def index(request):
    if request.method == 'GET':
        form = NewsArticleForm()
        return render(request, 'fake_news_detection/index.html', {'form': form})


def result(request):
    form_params = request.GET
    news_text = form_params.get('news_text', '')

    # Transform and Predict
    vec_news_text = tfidf_vectorizer.transform([news_text])
    ans = pac.predict(vec_news_text)

    # Cast to string to prevent JSON serialization errors (np.bool_ fix)
    prediction_result = str(ans[0])

    context = {
        'ans': prediction_result,
        'form_params': form_params
    }

    # Store in session for the satisfaction feedback loop
    request.session['results'] = context

    return render(request, "fake_news_detection/result.html", context)


def satisfaction(request):
    # Retrieve data from session safely
    results = request.session.get('results')

    if not results:
        return HttpResponse("No session data found. Please perform a fact-check first.")

    args_sent_by_user = request.GET

    if "user_choice" in args_sent_by_user:
        print(f"[+] Feedback received from user. Saving to DB...")

        # Extracting data for the database
        newspaper = results['form_params'].get('newspaper')
        category = results['form_params'].get('category')
        news_text = results['form_params'].get('news_text')
        label = results['ans']

        # Save the prediction to the database for future analysis
        NewsArticle.objects.create(
            newspaper=newspaper,
            category=category,
            news_text=news_text,
            label=label
        )

    return render(request, "fake_news_detection/satisfaction.html", {'args_sent_by_user': args_sent_by_user})