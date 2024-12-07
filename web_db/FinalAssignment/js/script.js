// 共通のJavaScript処理をここに記述
function openDeleteModal(medicationId) {
    const deleteFormIdField = document.getElementById('deleteFormId');
    if (deleteFormIdField) {
        deleteFormIdField.value = medicationId;
        const deleteModalElement = document.getElementById('deleteModal');
        if (deleteModalElement) {
            const deleteModal = new bootstrap.Modal(deleteModalElement);
            deleteModal.show();
        }
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const deleteAccountButton = document.getElementById("deleteAccountButton");
    const deleteModal = document.getElementById("deleteModal");
    const closeModal = document.getElementById("closeModal");
    const cancelDelete = document.getElementById("cancelDelete");

    // deleteAccountButton が存在する場合のみ処理を実行
    if (deleteAccountButton && deleteModal) {
        // モーダルを開く
        deleteAccountButton.addEventListener("click", function () {
            deleteModal.classList.remove("hidden");
        });

        // モーダルを閉じる
        if (closeModal) {
            closeModal.addEventListener("click", function () {
                deleteModal.classList.add("hidden");
            });
        }

        if (cancelDelete) {
            cancelDelete.addEventListener("click", function () {
                deleteModal.classList.add("hidden");
            });
        }

        // モーダル外をクリックしたときも閉じる
        window.addEventListener("click", function (event) {
            if (event.target === deleteModal) {
                deleteModal.classList.add("hidden");
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".use-preset-button");

    if (buttons.length > 0) {
        buttons.forEach((button) => {
            button.addEventListener("click", function (event) {
                event.preventDefault(); // フォーム送信を一時停止
                const form = button.closest("form");
                const originalText = button.textContent;

                // ボタンを無効化
                button.disabled = true;
                button.textContent = "処理中...";
                button.classList.add("btn-warning");

                // 3秒間クリックを防止し、フォームを送信
                setTimeout(() => {
                    form.submit();
                }, 3000);
            });
        });
    }
});