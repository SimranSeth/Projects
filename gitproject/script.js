function fetchRepositories() {
    const username = document.getElementById('usernameInput').value;
    const repositoriesList = document.getElementById('repositoriesList');

    if (username.trim() === '') {
        alert('Please enter a GitHub username.');
        return;
    }

    const apiUrl = `https://api.github.com/users/${username}/repos`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(repositories => {
            displayRepositories(repositoriesList, repositories);
        })
        .catch(error => {
            console.error('Error fetching repositories:', error);
            alert('Error fetching repositories. Please try again.');
        });
}

function displayRepositories(container, repositories) {
    container.innerHTML = ''; // Clear previous content

    repositories.forEach(repo => {
        const repoContainer = document.createElement('div');
        repoContainer.classList.add('repository');

        const repoTitle = document.createElement('h2');
        repoTitle.textContent = repo.name;

        const repoDescription = document.createElement('p');
        repoDescription.textContent = repo.description || 'No description available.';

        const repoUrl = document.createElement('a');
        repoUrl.href = repo.html_url;
        repoUrl.textContent = 'Go to Repository';

        repoContainer.appendChild(repoTitle);
        repoContainer.appendChild(repoDescription);
        repoContainer.appendChild(repoUrl);

        container.appendChild(repoContainer);
    });
}
