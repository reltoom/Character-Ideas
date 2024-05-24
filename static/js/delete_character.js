document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.getElementsByClassName("delete-char-button");
    const deleteConfirm = document.getElementById("delete-char-confirm");
    const deleteModal = new bootstrap.Modal(document.getElementById("delete-char-modal"));
  
    for (let i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener("click", (e) => {
            e.preventDefault(); // Preventing the default anchor behavior otherwise throws 404 error
            const characterSlug = e.target.getAttribute("data-character-slug");
            const characterTitle = e.target.closest('.card-body').querySelector('.image-title').innerText;
            const characterTitlePlaceholder = document.getElementById("character-title-placeholder");
            characterTitlePlaceholder.innerText = characterTitle;
            // Ensure characterSlug is not undefined before setting deleteConfirm href
            if (characterSlug) {
                // Set the delete confirmation URL properly
                deleteConfirm.href = `/${characterSlug}/delete/`;
                deleteModal.show();
            } else {
                console.error("Character slug is undefined.");
            }
        });
    }
});