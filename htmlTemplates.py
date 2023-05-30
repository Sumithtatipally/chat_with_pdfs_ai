css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
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
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://lh4.googleusercontent.com/QwxDAV7dl7GXj4pjTS2sO4nJn-iixM6WFvTHiX7UQRr2AHgMRjioH5TRIOuv4HnabY0fJu3YFGFRNW6h_HOJgvVjiqTqjk4Y1mo4vHXbdtwMPVDJFHBxuCgmcmhFPQWwHw=w1280">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''