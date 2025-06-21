document.addEventListener('DOMContentLoaded', () => {
    // --- Get references to all necessary elements ---
    const chatbotButton = document.getElementById('chatbot-button');
    const chatbotWindow = document.getElementById('chatbot-window');
    const closeChatbotBtn = document.getElementById('close-chatbot-btn');

    const cardModal = document.getElementById('card-modal');
    const closeCardModalBtn = document.getElementById('close-card-modal-btn');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');
    const modalLinks = document.getElementById('modal-links');
    const serviceCards = document.querySelectorAll('.card-hover-effect'); // Select all cards
    const heartSVGs = document.querySelectorAll('.heart-icon svg'); // Select all heart SVGs

    // --- Chatbot Logic (duplicated here because it's on both pages) ---
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
    
    // --- Heart Icon Toggle Logic ---
    heartSVGs.forEach(heartSVG => {
        heartSVG.addEventListener('click', (event) => {
            event.stopPropagation(); // Prevent card click event from firing

            heartSVG.classList.toggle('is-filled'); // Toggle a custom class to indicate its state

            if (heartSVG.classList.contains('is-filled')) {
                heartSVG.setAttribute('fill', '#ef4444'); // Tailwind red-500 equivalent
                heartSVG.setAttribute('stroke', '#ef4444'); // Also set stroke to red for a full look
            } else {
                heartSVG.setAttribute('fill', 'none'); // No fill (transparent)
                heartSVG.setAttribute('stroke', '#dc2626'); // Original red stroke color (Tailwind red-600 equivalent)
            }
        });
    });

    // --- Card Modal Logic ---
    const serviceData = {
        'monitoring': {
            title: 'Proactive Monitoring',
            description: 'Detailed insights into system health and performance metrics across all layers of our infrastructure.',
            links: [
                { text: 'Dashboard Overview', url: '#' },
                { text: 'Alerting Configuration Guide', url: '#' },
                { text: 'Log Aggregation Best Practices', url: '#' },
                { text: 'Metric Collection Standards', url: '#' },
                { text: 'SLO/SLA Reporting', url: '#' },
                { text: 'Synthetic Monitoring Setup', url: '#' }
            ]
        },
        'incident-response': {
            title: 'Incident Response',
            description: 'Our streamlined process for detecting, responding to, and resolving critical incidents with minimal impact.',
            links: [
                { text: 'On-Call Schedule', url: '#' },
                { text: 'Incident Communication Protocol', url: '#' },
                { text: 'Post-Mortem Templates', url: '#' },
                { text: 'Runbook Library', url: '#' },
                { text: 'Incident Management Tool', url: '#' },
                { text: 'War Room Access', url: '#' },
                { text: 'Major Incident Retrospectives', url: '#' }
            ]
        },
        'automation': {
            title: 'Eliminating Toil',
            description: 'Automating repetitive manual tasks and workflows to improve efficiency and reduce human error.',
            links: [
                { text: 'Automation Playbooks', url: '#' },
                { text: 'CI/CD Pipeline Status', url: '#' },
                { text: 'Infrastructure as Code Repository', url: '#' },
                { text: 'Automated Testing Framework', url: '#' },
                { text: 'Deployment Automation', url: '#' },
                { text: 'Self-Service Portals', url: '#' },
                { text: 'Toil Reduction Initiatives', url: '#' },
                { text: 'Script Library', url: '#' }
            ]
        },
        'capacity-planning': {
            title: 'Capacity Planning',
            description: 'Strategic planning to ensure our systems can handle current and future user loads and data growth efficiently.',
            links: [
                { text: 'Current Resource Utilization', url: '#' },
                { text: 'Forecasted Growth Reports', url: '#' },
                { text: 'Scaling Strategies', url: '#' },
                { text: 'Cost Optimization Analysis', url: '#' },
                { text: 'Performance Testing Results', url: '#' },
                { text: 'Infrastructure Expansion Plans', url: '#' },
                { text: 'Database Sharding Proposals', url: '#' },
                { text: 'CDN Usage Metrics', url: '#' },
                { text: 'Load Balancer Configurations', url: '#' },
                { text: 'Autoscaling Group Settings', url: '#' }
            ]
        }
    };

    const openCardModal = (cardId) => {
        const data = serviceData[cardId];
        if (data) {
            modalTitle.textContent = data.title;
            modalDescription.textContent = data.description;
            modalLinks.innerHTML = ''; // Clear previous links
            data.links.forEach(link => {
                const linkElement = document.createElement('a');
                linkElement.href = link.url;
                linkElement.textContent = link.text;
                linkElement.target = "_blank"; // Open in new tab
                linkElement.classList.add('block', 'p-3', 'bg-gray-50', 'hover:bg-blue-100', 'rounded-md', 'text-blue-700', 'font-medium', 'transition-colors', 'duration-200');
                modalLinks.appendChild(linkElement);
            });
            cardModal.classList.remove('hidden', 'modal-leave-to');
            cardModal.classList.add('modal-enter-active');
            setTimeout(() => {
                cardModal.classList.remove('modal-enter-from');
            }, 10);
        }
    };

    const closeCardModal = () => {
        cardModal.classList.add('modal-leave-active');
        cardModal.classList.add('opacity-0', 'modal-leave-to');
        setTimeout(() => {
            cardModal.classList.add('hidden');
            cardModal.classList.remove('modal-enter-active', 'modal-leave-active', 'opacity-0');
        }, 300); // Should match CSS transition duration
    };

    serviceCards.forEach(card => {
        card.addEventListener('click', (event) => {
            // Check if the click originated from the heart icon
            if (!event.target.closest('.heart-icon')) {
                const cardId = card.dataset.cardId;
                openCardModal(cardId);
            }
        });
    });

    closeCardModalBtn.addEventListener('click', closeCardModal);
    // Close modal when clicking outside of it
    cardModal.addEventListener('click', (event) => {
        if (event.target === cardModal) {
            closeCardModal();
        }
    });
});