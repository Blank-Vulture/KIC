// 年齢計算のためのヘルパー関数
function calculateAge(birthday) {
    const birthDate = new Date(birthday);
    const diff = Date.now() - birthDate.getTime();
    const ageDate = new Date(diff);
    return Math.abs(ageDate.getUTCFullYear() - 1970);
}

// データ表示処理
function displayData(data, requestType) {
    const container = document.getElementById('dataContainer');
    container.innerHTML = '';

    data.forEach((item, index) => {
        const col = document.createElement('div');
        col.className = 'col-lg-4 col-md-6 col-sm-12 mb-4';

        let content = '';
        switch (requestType) {
            case 'address':
                content = `
                    <p><strong>住所情報:</strong></p>
                    <p>住所: ${item.street} ${item.city}, ${item.zipcode}, ${item.country} (${item.country_code})</p>
                    <p>緯度: ${item.latitude}, 経度: ${item.longitude}</p>`;
                break;
            case 'books':
                content = `
                    <p><strong>書籍情報:</strong></p>
                    <p>タイトル: ${item.title}<br>著者: ${item.author}</p>
                    <p>ISBN: ${item.isbn}<br>ジャンル: ${item.genre}</p>
                    <p>出版社: ${item.publisher} (${item.published})</p>
                    <p>説明: ${item.description}</p>`;
                break;
            case 'companies':
                if (item.addresses && item.addresses.length > 0) {
                    const address = item.addresses[0];
                    content = `
                        <p><strong>会社情報:</strong></p>
                        <p>会社名: ${item.name}<br>Email: ${item.email}<br>VAT: ${item.vat}</p>
                        <p>電話: ${item.phone}</p>
                        <p>住所: ${address.street}, ${address.city}, ${address.zipcode}, ${address.country} (${address.country_code})</p>
                        <p>ウェブサイト: ${item.website}<br><img src="${item.image}" alt="会社画像" class="img-fluid"></p>
                        <p><strong>コンタクト担当者:</strong> ${item.contact.firstname} ${item.contact.lastname}</p>
                        <p>Email: ${item.contact.email}<br>電話: ${item.contact.phone}<br>住所: ${item.contact.address.street} ${item.contact.address.city}</p>`;
                }
                break;
            case 'creditCards':
                content = `
                    <p><strong>クレジットカード情報:</strong></p>
                    <p>カードタイプ: ${item.type}<br>カード番号: ${item.number}<br>有効期限: ${item.expiration}<br>カード所有者: ${item.owner}</p>`;
                break;
            case 'images':
                content = `
                    <p><strong>画像情報:</strong></p>
                    <p>タイトル: ${item.title}<br>説明: ${item.description}</p>
                    <img src="${item.url}" alt="画像" class="img-fluid">`;
                break;
            case 'persons':
                const age = calculateAge(item.birthday);
                content = `
                    <p><strong>人物情報:</strong></p>
                    <p>名前: ${item.firstname} ${item.lastname} (${item.gender})</p>
                    <p>年齢: ${age}歳<br>誕生日: ${item.birthday}</p>
                    <p>Email: ${item.email}<br>電話: ${item.phone}</p>
                    <p>住所: ${item.address.street}, ${item.address.city}, ${item.address.zipcode}, ${item.address.country} (${item.address.country_code})</p>
                    <p>ウェブサイト: ${item.website}<br><img src="${item.image}" alt="人物画像" class="img-fluid"></p>`;
                break;
            case 'places':
                content = `
                    <p><strong>場所情報:</strong></p>
                    <p>緯度: ${item.latitude}, 経度: ${item.longitude}</p>`;
                break;
            case 'products':
                content = `
                    <p><strong>商品情報:</strong></p>
                    <p>商品名: ${item.name}<br>説明: ${item.description}</p>
                    <p>価格: ${item.price} 円 (税込み: ${item.net_price} 円)</p>
                    <p>UPC: ${item.upc}<br>EAN: ${item.ean}</p>
                    <p>タグ: ${item.tags.join(', ')}</p>`;
                item.images.forEach(image => {
                    content += `<img src="${image.url}" alt="${image.title}" class="img-fluid mt-2">`;
                });
                break;
            case 'texts':
                content = `
                    <p><strong>テキスト情報:</strong></p>
                    <p>タイトル: ${item.title}<br>著者: ${item.author}<br>ジャンル: ${item.genre}</p>
                    <p>${item.content}</p>`;
                break;
            case 'users':
                content = `
                    <p><strong>ユーザー情報:</strong></p>
                    <p>名前: ${item.firstname} ${item.lastname} (ユーザー名: ${item.username})</p>
                    <p>Email: ${item.email}<br>IPアドレス: ${item.ip}</p>
                    <p>MACアドレス: ${item.macAddress}</p>
                    <p>ウェブサイト: ${item.website}<br><img src="${item.image}" alt="ユーザー画像" class="img-fluid"></p>`;
                break;
            default:
                content = `<p>データがありません</p>`;
        }

        col.innerHTML = `
            <div class="card bg-light">
                <div class="card-body">
                    <h5 class="card-title text-success">${requestType} ${index + 1}</h5>
                    ${content}
                </div>
            </div>
        `;
        container.appendChild(col);
    });
}

// 生のリクエスト結果をコードブロックに表示
function displayRawData(rawData) {
    const rawDataContainer = document.getElementById('rawData');
    rawDataContainer.textContent = JSON.stringify(rawData, null, 2);
}

// データ取得処理
document.getElementById('dataForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const requestType = document.getElementById('requestType').value;
    const quantity = document.getElementById('quantity').value;
    const locale = document.getElementById('locale').value;
    const seed = document.getElementById('seed').value;

    let apiUrl = `https://fakerapi.it/api/v2/${requestType}?_quantity=${quantity}&_locale=${locale}`;
    if (seed) apiUrl += `&_seed=${seed}`;

    // APIリクエストの実行とエラーハンドリング
    try {
        const response = await axios.get(apiUrl);
        const data = response.data.data;
        displayData(data, requestType);
        displayRawData(response.data);
    } catch (error) {
        console.error("データの取得に失敗しました:", error);
    }
});