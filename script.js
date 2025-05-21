document.addEventListener('DOMContentLoaded', () => {
    const bookmarkletContainer = document.getElementById('bookmarklet-container');

    // Fetch bookmarklet data from the backend API
    fetch('/bookmarklets')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(bookmarklets => {
            if (bookmarklets.length === 0) {
                bookmarkletContainer.innerHTML = '<p>No bookmarklets found.</p>';
                return;
            }
            bookmarklets.forEach(bookmarklet => {
                const card = document.createElement('div');
                card.className = 'bookmarklet-card';

                const title = document.createElement('h3');
                title.textContent = bookmarklet.title;
                card.appendChild(title);

                const description = document.createElement('p');
                // Use innerHTML for description to render <br> tags if present
                description.innerHTML = bookmarklet.description || 'No description available.';
                card.appendChild(description);

                const actionsContainer = document.createElement('div');
                actionsContainer.className = 'actions';

                if (bookmarklet.code_snippets && bookmarklet.code_snippets.length > 0) {
                    bookmarklet.code_snippets.forEach((snippet, index) => {
                        // Create a container for each snippet if there are multiple
                        const snippetContainer = document.createElement('div');
                        snippetContainer.className = 'code-snippet-container';

                        // Add a label if there are multiple snippets for one bookmarklet
                        if (bookmarklet.code_snippets.length > 1) {
                            const snippetLabel = document.createElement('p');
                            snippetLabel.textContent = `Snippet ${index + 1}:`;
                            snippetContainer.appendChild(snippetLabel);
                        }
                        
                        const bookmarkletLink = document.createElement('a');
                        bookmarkletLink.href = snippet;
                        // Try to generate a user-friendly name for the bookmarklet link
                        // This might be the main title or a more specific one if available
                        let linkName = bookmarklet.title.replace(/[^a-zA-Z0-9]/g, ''); // Basic sanitize
                        if (bookmarklet.code_snippets.length > 1) {
                           linkName += `_${index+1}`;
                        }
                        bookmarkletLink.textContent = `Drag ${linkName}`;
                        bookmarkletLink.title = `Drag this to your bookmarks bar: ${bookmarklet.title}`;
                        snippetContainer.appendChild(bookmarkletLink);

                        const copyButton = document.createElement('button');
                        copyButton.className = 'copy-code-btn';
                        copyButton.textContent = 'Copy Code';
                        copyButton.addEventListener('click', () => {
                            navigator.clipboard.writeText(snippet)
                                .then(() => {
                                    alert('Bookmarklet code copied to clipboard!');
                                })
                                .catch(err => {
                                    console.error('Failed to copy code: ', err);
                                    alert('Failed to copy code. See console for details.');
                                });
                        });
                        snippetContainer.appendChild(copyButton);
                        actionsContainer.appendChild(snippetContainer);
                    });
                }
                card.appendChild(actionsContainer);
                bookmarkletContainer.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Error fetching bookmarklets:', error);
            bookmarkletContainer.innerHTML = `<p>Error loading bookmarklets: ${error.message}. Check the console for more details. Make sure the backend server is running and the /bookmarklets endpoint is available.</p>`;
        });
});
