from django.shortcuts import render, get_object_or_404,redirect
from . models import ChatGroup, GroupMessage,UploadFile
from django.contrib.auth.decorators import login_required
from . forms import *


@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup,group_name="test")

    # through this code it connect the parent to child ( models )
    chat_messages = chat_group.chatsss.all()[:30]
    # 30 messages
    form = ChatmessageCreateForm()

    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message':message,
                'user': request.user
            }
            return render(request,'chat-message-p.html',context)

    return render(request,'chat.html',{'chat_messages':chat_messages,'form':form})


def upload_file(request):
    if request.method == "POST":
        file = request.FILES['file']
        upload_file = UploadFile.objects.create(student_id=request.user.id,assign_file=file)
        return redirect('chat_view')
    else:
        return render(request,'upload-file.html')

