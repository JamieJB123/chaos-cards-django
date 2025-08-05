const editButtons = document.querySelectorAll('.edit-btn');
const cardForm = document.getElementById('card-form');
const formTitle = document.getElementById('form-title');
const formTitleInput = document.getElementById('id_title');
const formContent = document.getElementById('id_content');
const submitButton = document.getElementById('submit-btn');

const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteButtons = document.querySelectorAll('.delete-btn');
const deleteConfirm = document.getElementById('deleteConfirm');

/**
 * Initialises edit functionality for the provided edit buttons.
 * It populates the form fields with the card's data for editing.
 * Retrieves the associated card's ID on click from buttons data attribute.
 * Fetches the content of the corresponding card and populates the form fields.
 * Updates the form Title to "Edit Card"
 * Sets the submit button text to "Update Card"
 * Sets the form action attritbute to the card's update URL ('edit_card/{card_id}/')
 */

for (let button of editButtons) {
    button.addEventListener('click', (e) => {
        // Retrieve card ID from button's data atttribute
        let cardId = e.target.dataset.cardId;
        // Retrieve card title and content from DOM
        let cardTitle = document.getElementById(`card-title${cardId}`)
        let cardContent = document.getElementById(`card-content${cardId}`);
        // Populate form fields with card data
        formTitleInput.value = cardTitle.innerText;
        formContent.value = cardContent.innerText;
        // Alter form title and submit button text
        formTitle.innerText = "Edit Card";
        submitButton.innerText = "Update Card";
        // Set form action to the card's update URL
        cardForm.setAttribute('action', `/my-cards/edit_card/${cardId}/`);
        // Refocus on title input field for user convenience
        formTitleInput.focus();
})
}

// Delete functionality for delete buttons
for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let cardId = e.target.dataset.cardId;
        deleteConfirm.href = `/my-cards/delete-card/${cardId}/`;
        deleteModal.show();
    })
}
