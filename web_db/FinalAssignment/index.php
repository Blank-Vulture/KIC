<?php
$pageTitle = "トップページ";
include 'header.php';
?>
<div class="container mt-4">
    <div class="text-center">
        <h1 class="text-sleek">残薬管理アプリへようこそ！</h1>
        <p class="text-muted">薬品の在庫管理や服用履歴を簡単に記録できます。</p>
        <a href="register.php" class="btn btn-outline-primary sleek-btn">新規登録</a>
        <a href="login.php" class="btn btn-outline-secondary sleek-btn">ログイン</a>
    </div>

    <!-- モダンで詳細なリクエストモニター -->
    <div class="mt-5">
        <h3 class="text-sleek">リクエストモニター</h3>
        <div class="monitor-container">
            <div class="monitor-header">
                <span class="short-column">種類</span>
                <span>URL</span>
                <span>ステータス</span>
            </div>
            <div class="monitor-body" id="requestMonitor">
                <div class="monitor-row">リクエストを監視中...</div>
            </div>
        </div>
    </div>
</div>

<style>
    /* モニターコンテナのデザインは以前と同じ */
    .monitor-header {
        display: flex;
        justify-content: space-between;
        padding: 10px 15px;
        border-bottom: 2px solid #333333;
        background-color: #f3f3f3;
        font-weight: bold;
    }

    .monitor-body {
        max-height: 300px;
        overflow-y: auto;
    }

    .monitor-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 15px;
        border-bottom: 1px solid #e0e0e0;
        transition: background-color 0.3s ease;
        align-items: center;
    }

    .monitor-row .short-column {
        flex: 0 0 80px;
        text-align: center;
    }

    .monitor-row .url-column {
        flex: 1 1 auto;
        white-space: pre-wrap;
        word-break: break-word;
    }

    .monitor-row .status-column {
        flex: 0 0 150px;
        text-align: right;
    }

    /* ステータスの色分け */
    .text-success {
        color: #28a745 !important;
    }

    .text-danger {
        color: #dc3545 !important;
    }

    .text-warning {
        color: #ffc107 !important;
    }

    /* アニメーション */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .monitor-row {
        animation: slideIn 0.5s ease-in-out;
    }
</style>

<script>
    const monitorContainer = document.getElementById("requestMonitor");

    // ネットワークリクエストモニタリング
    (function () {
        const originalFetch = window.fetch;

        // fetch監視
        window.fetch = async function (...args) {
            const requestUrl = args[0];
            try {
                const response = await originalFetch(...args);
                logRequest("fetch", requestUrl, response.status, false);
                return response;
            } catch (error) {
                logRequest("fetch", requestUrl, "エラー", false);
                throw error;
            }
        };

        // XMLHttpRequest監視
        const originalOpen = XMLHttpRequest.prototype.open;
        XMLHttpRequest.prototype.open = function (method, url, ...rest) {
            this._requestUrl = url;
            this.addEventListener("load", () => logRequest("XMLHttpRequest", url, this.status, false));
            this.addEventListener("error", () => logRequest("XMLHttpRequest", url, "エラー", false));
            originalOpen.apply(this, [method, url, ...rest]);
        };
    })();

    // ページ読み込み時にロードされたリソースを表示
    document.addEventListener("DOMContentLoaded", () => {
        const resources = performance.getEntriesByType("resource");
        resources.forEach(resource => {
            const isCacheHit = resource.transferSize === 0;
            const status = isCacheHit ? "キャッシュ" : resource.duration > 0 ? "成功" : "エラー";
            logRequest(resource.initiatorType, resource.name, status, isCacheHit);
        });
    });

    // ログを記録
    function logRequest(type, url, status, isCache) {
        const row = document.createElement("div");
        row.className = "monitor-row";
        row.innerHTML = `
            <span class="short-column ${getStatusClass(status)}">${type}</span>
            <span class="url-column">${url}</span>
            <span class="status-column ${getStatusClass(status)}">${status}</span>
        `;
        monitorContainer.appendChild(row);
        monitorContainer.scrollTop = monitorContainer.scrollHeight;
    }

    // ステータスに応じてクラスを設定
    function getStatusClass(status) {
        if (status === "エラー") return "text-danger";
        if (status === "キャッシュ") return "text-warning";
        if (status === "成功") return "text-success";
        return "text-primary";
    }
</script>

<?php include 'footer.php'; ?>