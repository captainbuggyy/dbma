// Inside {% block script %}
function openRejectModal(modalId) {
    const rejectReasonModal = document.getElementById(modalId);
    rejectReasonModal.style.display = 'block';
}

function closeRejectModal(modalId) {
    const rejectReasonModal = document.getElementById(modalId);
    rejectReasonModal.style.display = 'none';
}

function validateRejectReason(farmerId) {
    const rejectReasonInput = document.getElementById(`rejectReason_${farmerId}`);
    if (rejectReasonInput.value.trim() === '') {
        alert('Please provide a reason for rejection.');
        return false;
    }
    return true;
}
