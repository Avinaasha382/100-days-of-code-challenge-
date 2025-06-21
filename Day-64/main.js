document.addEventListener('DOMContentLoaded', () => {
    const chatbotButton = document.getElementById('chatbot-button');
    const chatbotWindow = document.getElementById('chatbot-window');
    const closeChatbotBtn = document.getElementById('close-chatbot-btn');

    // --- Chatbot Logic ---
    const toggleChatbot = () => {
        if (chatbotWindow.classList.contains('hidden')) {
            chatbotWindow.classList.remove('hidden');
            setTimeout(() => {
                chatbotWindow.classList.remove('opacity-0', 'translate-y-4');
            }, 10); 
        } else {
            chatbotWindow.classList.add('opacity-0', 'translate-y-4');
            setTimeout(() => {
                chatbotWindow.classList.add('hidden');
            }, 300);
        }
    };

    // Attach chatbot event listeners
    if (chatbotButton) { // Check if element exists on this page
        chatbotButton.addEventListener('click', toggleChatbot);
    }
    if (closeChatbotBtn) { // Check if element exists on this page
        closeChatbotBtn.addEventListener('click', toggleChatbot);
    }
});