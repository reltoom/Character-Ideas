document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.getElementsByClassName("delete-char-button");
    const deleteConfirm = document.getElementById("delete-char-confirm");
    const deleteModal = new bootstrap.Modal(document.getElementById("delete-char-modal"));
    const modalBody = document.getElementById("delete-char-modal-body");
  
    for (let i = 0; i < deleteButtons.length; i++) {
      deleteButtons[i].addEventListener("click", (e) => {
        const characterSlug = e.target.getAttribute("data-character_slug");
        const characterTitle = modalBody.getAttribute("data-character_title");
        deleteConfirm.href = `${deleteConfirm.dataset.baseUrl}${characterSlug}`;
        modalBody.innerText = `Are you sure you want to delete ${characterTitle}?`;
        deleteModal.show();
      });
    }
});