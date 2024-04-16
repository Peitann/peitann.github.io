 const mntoggle = document.querySelector('.menu-toggle input');
 const nav = document.querySelector('nav ul');

mntoggle.addEventListener('click',function(){
    nav.classList.toggle('menushow');
})

$(document).ready(function(){
    // Load JSON data and insert into table
    $.getJSON("data/republika_news.json", function(data){
        $.each(data, function(index, item){
            var row = $("<tr>");
            row.append($("<td>").text(item.judul));
            row.append($("<td>").text(item.kategori));
            row.append($("<td>").text(item.waktu_publish));
            row.append($("<td>").text(item.waktu_scraping));
            $("#newsTable tbody").append(row);
        });
    });
});

function sortTable(columnIndex) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("newsTable");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[columnIndex];
            y = rows[i + 1].getElementsByTagName("td")[columnIndex];
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                shouldSwitch= true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

