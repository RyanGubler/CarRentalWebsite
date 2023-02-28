var startDatePicker;
var endDatePicker;
var startDate;
var endDate;

window.onload = function() {
    function pikadayCalender(){
        startDatePicker = new Pikaday({ field: document.getElementById('start-date'),
                                        minDate: moment().toDate(),
                                        format: 'MM/DD/YYYY'});
        endDatePicker = new Pikaday({ field: document.getElementById('end-date'),
                                        format: 'MM/DD/YYYY'});
        startDatePicker.setMinDate(new Date());
        endDatePicker.setMinDate(new Date())
        startDatePicker._o.onSelect = function(date){
            endDatePicker.setMinDate(date);
        }
        endDatePicker._o.onSelect = function(date){
            startDatePicker.setMaxDate(date);
        }
    }
    pikadayCalender();
}