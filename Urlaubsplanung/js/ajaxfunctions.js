//On Page load - register listeners and load existing videos in datatable
$(document).ready(function() {
    loadDataTable();
    loadPersonDataTable();
    loadSortiertPrio();
    updateSelect();
    //process the form newVideo
    $("#newUZ").submit(function(event) {
        postUZ(event);
    });

    $('#updateUZ').submit(function(event) {
        updateUZ(event);
    });

    $('#deleteUZ').click(function(event) {
        deleteUZ(event);
    });

    //Load Datatable
    $('#loadtable').click(function() {
        loadDataTable();
    });

    $('#loadPersonDataTable').click(function() {
        loadDataTable();
    });

    $('#loadSortiertPrio').click(function() {
        loadDataTable();
    });
});

function postUZ(event) {
    // get the form data
    var formData = {
        'title': $('input[name=title]').val(),
        'description': $('textarea[name=description]').val(),
        'age_rating': $('input[name=age_rating]').val(),
        'genre': $('input[name=genre]').val()
    };
    // process the form
    $.ajax({
        type: 'POST', // define the type of HTTP verb we want to use (POST for our form)
        contentType : 'application/json',
        url: '/video', //url where we want to POST
        data: JSON.stringify(formData), // data we want to POST
        success: function( data, textStatus, jQxhr ){
            loadDataTable();
            updateSelect();
        },
        error: function( jqXhr, textStatus, errorThrown ){
            console.log(errorThrown);
        }
    });
    // stop the form from submitting the normal way and refreshing the page
    event.preventDefault();
}

function updateVideo(event) {
    var id = $('#vnr').val();
    var updatedData = {
        'title': $('input[name=title_update]').val(),
        'description': $('textarea[name=description_update]').val(),
        'age_rating': $('input[name=age_rating_update]').val(),
        'genre': $('input[name=genre_update]').val()
    };
    $.ajax({
      url: '/video/' + id,
      type: 'PUT',
      data: JSON.stringify(updatedData),
      success: function(updatedData) {
        loadDataTable();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error updating entry with ID ${id}: ${errorThrown}');
      }
    });
}

function deleteVideo(event) {
    var id = $('#vnr_del').val();

    $.ajax({
      url: '/video/' + id,
      type: 'DELETE',
      success: function() {
        loadDataTable();
        updateSelect();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error deleting instance with ID ${instanceId}: ${errorThrown}');
      }
    });
}


function loadDataTable() {
    var table = $('#uztable').DataTable({
        destroy: true,
        "ajax": {
            "url": "/urlaubsziele",  //URL
            "dataSrc": "" // Cause of flat JsonObjects
        },
        "columns": [
            { "data": "uzid" },
            { "data": "land" },
            { "data": "ort" },
            { "data": "distanz" },
            { "data": "transportmittel"},
            { "data": "kostenrahmen"},
            { "data": "kurzbeschreibung"},
            { "data": "startdatum"},
            { "data": "enddatum"}


        ]
    });
}


function loadPersonDataTable() {
    var table = $('#Usertabelle').DataTable({
        destroy: true,
        "ajax": {
            "url": "/persons",  //URL
            "dataSrc": "" // Cause of flat JsonObjects
        },
        "columns": [
            { "data": "pid" },
            { "data": "name" },



        ]
    });
}

function loadSortiertPrio() {
    var table = $('#SortiertPrioTabelle').DataTable({
        destroy: true,
        "ajax": {
            "url": "/sortiertprio",  //URL
            "dataSrc": "" // Cause of flat JsonObjects
        },
        "columns": [
            { "data": "uz_uzid" },
            { "data": "prio" },



        ]
    });
}


function updateSelect() {
    $.ajax({
    url: "/videonumbers", // replace with your server-side script URL
    type: "GET",
    dataType: "json",
    success: function(data) {
      var select = $("#vnr"); // select element to populate
      var select_del = $("#vnr_del");
      // clear any existing options
      select.empty();
      select_del.empty();
      // add new options based on data
      data.forEach(function(entry) {
        var option = $("<option></option>").attr("value", entry.id).text(entry);
        var option_del = $("<option></option>").attr("value", entry.id).text(entry);
        select.append(option);
        select_del.append(option_del);
      });
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log("Error fetching data: " + textStatus + ", " + errorThrown);
    }
  });
}

