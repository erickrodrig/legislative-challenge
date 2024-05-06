document.addEventListener('DOMContentLoaded', function () {
    let table = document.getElementById('table');

    if (table) {
        new DataTable(table, {
            colReorder: true,
            responsive: true,
            hover: true,
            pageLength: 20,
            pagingType: 'simple_numbers',
            layout: {
                topStart: 'buttons'
            },
            buttons: ['print', 'csv'],
            columnDefs: [
                {
                    className: "text-center",
                    targets: "_all"
                },
            ]
        });
    }
});
