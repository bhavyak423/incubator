from django.http import HttpResponse
from .forms import VidClipUploadForm
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def uploadVideo(request):
    if request.method == "POST":
        form = VidClipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = request.FILES["vid"]
            query = form.cleaned_data["query"]
            uploadToS3(video)
            return HttpResponse(
                f"Received and uploaded video: {video}, query: {query} "
            )
        else:
            logger.error("Invalid form")


def uploadToS3(video):
    logger.info("uploading video...")
