/* Функция закрывает по нажатие на кнопку модальное окно */
function bclose(numModel) {
    let namePopup = "#popup-main-modal-"+numModel
	$(namePopup).bPopup().close();
	return false;
}

/* Функция показывает модальное окно по нажатию на кнопку */
function bopen(numModel) {
    let namePopup = "#popup-main-modal-"+numModel
    $(namePopup).bPopup();
	return false;
}
