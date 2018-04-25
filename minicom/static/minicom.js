var Minicom = {
  register: function(user_email) {
    $.post('http://localhost:8000/api/ping', { email: user_email }).done(
      function(response) {
        $.each(response['unread_messages'], function(index, message) {
          alert(message.message);
          Minicom.mark_read(user_email, message.message_id);
        });
      },
    );
  },

  mark_read: function(user_email, message_id) {
    $.post('http://localhost:8000/api/read', {
      email: user_email,
      message_id: message_id,
    });
  },

  // for user to send message to admin
  sendMessage: function(user_email, message) {
    $.post('http://localhost:8000/api/send', {
      to_user: user_email,
      message: message,
      direction: 'FROM_USER',
    });
  },

  getConversation: function(user_email) {
    return $.post('http://localhost:8000/api/conversation', {
      email: user_email,
    });
  },
};
