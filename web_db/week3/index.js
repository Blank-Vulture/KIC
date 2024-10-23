document.addEventListener('DOMContentLoaded', () => {
    let areas = [];
    const searchInput = document.getElementById('searchInput');
    const suggestions = document.getElementById('suggestions');
    const weatherInfo = document.getElementById('weatherInfo');

    // areas.jsonを読み込む
    fetch('areas.json')
        .then(response => response.json())
        .then(data => {
            areas = data;
        })
        .catch(error => {
            console.error('エリアデータの読み込み中にエラーが発生しました:', error);
        });

    // リアルタイム検索のイベントリスナー
    searchInput.addEventListener('input', () => {
        const inputText = searchInput.value.trim();
        suggestions.innerHTML = '';

        if (inputText.length > 0) {
            const filteredAreas = areas.filter(area => area.name.includes(inputText));

            filteredAreas.forEach(area => {
                const suggestionItem = document.createElement('div');
                suggestionItem.classList.add('suggestion-item');
                suggestionItem.textContent = area.name;
                suggestionItem.dataset.code = area.code;

                suggestionItem.addEventListener('click', () => {
                    searchInput.value = area.name;
                    suggestions.innerHTML = '';
                    fetchWeather(area.code);
                });

                suggestions.appendChild(suggestionItem);
            });
        }
    });

    // 天気情報を取得する関数
    function fetchWeather(areaCode) {
        const forecastUrl = `https://www.jma.go.jp/bosai/forecast/data/forecast/${areaCode}.json`;
        const overviewUrl = `https://www.jma.go.jp/bosai/forecast/data/overview_forecast/${areaCode}.json`;

        Promise.all([
            fetch(forecastUrl).then(response => response.json()),
            fetch(overviewUrl).then(response => response.json())
        ])
            .then(([forecastData, overviewData]) => {
                displayWeather(forecastData, overviewData);
            })
            .catch(error => {
                console.error('天気情報の取得中にエラーが発生しました:', error);
            });
    }

    // 天気情報を表示する関数
    function displayWeather(forecastData, overviewData) {
        // forecastDataの解析
        const areaName = forecastData[0].timeSeries[0].areas[0].area.name;
        const weatherDescription = forecastData[0].timeSeries[0].areas[0].weathers[0];
        const weatherCode = forecastData[0].timeSeries[0].areas[0].weatherCodes[0];
        const temps = forecastData[0].timeSeries[2]?.areas[0]?.temps;
        const temp = temps ? temps[0] : 'N/A';

        // overviewDataの解析
        const overviewText = overviewData.text.replace(/\n/g, '<br>');

        // 天気情報の表示を更新
        weatherInfo.innerHTML = `
            <h2>${areaName}の天気</h2>
            <p class="weather-description">${weatherDescription}</p>
            <p class="temp">気温: ${temp}℃</p>
            <h3>概況</h3>
            <p class="overview">${overviewText}</p>
        `;

        // 天気コードに応じて背景色を変更
        changeBackgroundColor(weatherCode);
    }

    // 天気コードに基づいて背景色を変更する関数
    function changeBackgroundColor(weatherCode) {
        let bgColor;
        if (weatherCode.startsWith('1')) {
            bgColor = '#FFE4B5'; // 晴れ
        } else if (weatherCode.startsWith('2')) {
            bgColor = '#D3D3D3'; // くもり
        } else if (weatherCode.startsWith('3')) {
            bgColor = '#87CEFA'; // 雨
        } else if (weatherCode.startsWith('4')) {
            bgColor = '#B0C4DE'; // 雪
        } else {
            bgColor = '#FFFFFF'; // その他
        }

        // 背景色をフェードインで変更
        document.body.style.transition = 'background-color 0.5s ease';
        document.body.style.backgroundColor = bgColor;
    }
});