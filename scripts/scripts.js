function loadPage(page) {
    const contentDiv = document.getElementById('content');
    let pageUrl;

    if (page === 'project') {
        pageUrl = 'pages/project.html';
    } else if (page === 'lambda') {
        pageUrl = 'pages/lambda.html';
    } else if (page === 'services') {
        pageUrl = 'services.html';
    } else if (page === 'contact') {
        pageUrl = 'contact.html';
    }

    if (pageUrl) {
        fetch(pageUrl)
            .then(response => {
                if (!response.ok) throw new Error('Ошибка загрузки страницы');
                return response.text();
            })
            .then(data => {
                contentDiv.innerHTML = data;
            })
            .catch(error => {
                contentDiv.innerHTML = '<p>Произошла ошибка при загрузке страницы.</p>';
                console.error(error);
            });
    }
}
