import os
user_image_path = os.path.join("static", "images", "user_image.png")
bot_image_path = os.path.join("static", "images", "bot_image.png")

css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.chat-message.user {
    background-color: #2979ff;
    justify-content: flex-end;
}
.chat-message.bot {
    background-color: #4caf50;
}
.chat-message .avatar {
    width: 20%;
    margin-right: 10px;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
    border-radius: 10px;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <span style="font-size: 24px;">{BOT_SYMBOL}</span>
    </div>
    <div class="message">{MSG}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <span style="font-size: 24px;">{USER_SYMBOL}</span>
    </div>    
    <div class="message">{MSG}</div>
</div>
'''
