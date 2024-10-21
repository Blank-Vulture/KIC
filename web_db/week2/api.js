document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const word = document.getElementById('wordInput').value.trim();
    if (word) {
        searchWord(word);
    }
});

function searchWord(word) {
    const apiUrl = `https://api.dictionaryapi.dev/api/v2/entries/en/${word}`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('単語が見つかりませんでした');
            }
            return response.json();
        })
        .then(data => displayResult(data))
        .catch(error => {
            document.getElementById('result').innerHTML = `<p>${error.message}</p>`;
        });
}

function displayResult(data) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ''; // 以前の結果をクリア

    data.forEach(entry => {
        const wordElement = document.createElement('h2');
        wordElement.textContent = entry.word;
        resultDiv.appendChild(wordElement);

        entry.meanings.forEach(meaning => {
            const partOfSpeech = document.createElement('h3');
            partOfSpeech.textContent = meaning.partOfSpeech;
            resultDiv.appendChild(partOfSpeech);

            meaning.definitions.forEach(definition => {
                const definitionParagraph = document.createElement('p');
                definitionParagraph.textContent = definition.definition;
                resultDiv.appendChild(definitionParagraph);
            });
        });
    });
}