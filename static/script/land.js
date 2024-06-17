// document.addEventListener('DOMContentLoaded', () => {
//     const addLandButton = document.getElementById('addLandButton');
//     const addLandModal = document.getElementById('addLandModal');
//     const editLandModal = document.getElementById('editLandModal');
//     const addModalClose = addLandModal.getElementsByClassName('close')[0];
//     const editModalClose = editLandModal.getElementsByClassName('close')[0];

//     function openEditModal(id, address, surveyNumber) {
//         document.getElementById('editLandId').value = id;
//         document.getElementById('editLandAddress').value = address;
//         document.getElementById('editSurveyNumber').value = surveyNumber;
//         editLandModal.style.display = 'none';
//     }

//     // Event listeners to open/close modals
//     addLandButton.addEventListener('click', () => addLandModal.style.display = 'block');
//     addModalClose.addEventListener('click', () => addLandModal.style.display = 'none');
//     editModalClose.addEventListener('click', () => editLandModal.style.display = 'block');

//     // Close modals when clicking outside of them
//     window.addEventListener('click', (event) => {
//         if (event.target == addLandModal) addLandModal.style.display = 'none';
//         if (event.target == editLandModal) editLandModal.style.display = 'none';
//     });
// });

// Define the openEditModal function globally
function openEditModal(id, address, surveyNumber) {
    const editLandModal = document.getElementById('editLandModal');
    document.getElementById('editLandId').value = id;
    document.getElementById('editLandAddress').value = address;
    document.getElementById('editSurveyNumber').value = surveyNumber;
    editLandModal.style.display = 'block';
}

document.addEventListener('DOMContentLoaded', () => {
    const addLandButton = document.getElementById('addLandButton');
    const addLandModal = document.getElementById('addLandModal');
    const editLandModal = document.getElementById('editLandModal');
    const addModalClose = addLandModal.getElementsByClassName('close')[0];
    const editModalClose = editLandModal.getElementsByClassName('close')[0];

    // Event listeners to open/close modals
    addLandButton.addEventListener('click', () => addLandModal.style.display = 'block');
    addModalClose.addEventListener('click', () => addLandModal.style.display = 'none');
    editModalClose.addEventListener('click', () => editLandModal.style.display = 'none');

    // Close modals when clicking outside of them
    window.addEventListener('click', (event) => {
        if (event.target == addLandModal) addLandModal.style.display = 'none';
        if (event.target == editLandModal) editLandModal.style.display = 'none';
    });
});
