//On Page load - register listeners and load existing videos in datatable
$(document).ready(function() {
    loadDataTable();
    loadPersonDataTable();
    loadSortiertPrio();
    updateSelect();
    //process the form newVideo
    $("#NeuesUrlaubzieltabelle").submit(function(event) {
        alert('vor Click');
        postUZ(event);
    })

    $('#UpdateNeuesUrlaubzieltabelle').submit(function(event) {
        alert('vor Click');
        updateUZ(event);
    });

  $('#uz_delete').submit(function(event) {
      alert('vor Click');
      deleteUrlaubsvorschlag();
    });


  $("#vorschlag_anlegen").submit(function(event) {
      alert('vor Click');
      postVorschlag(event);
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

alert($('input[name="updateUrlaubszielNeu"]').val());
alert($('#NeuesUrlaubzieltabelle input[name="Startdatum"]').val());
alert($('#NeuesUrlaubzieltabelle select[name="land"]').val());

    // Holen Sie die Formulardaten
var formData = {
    'ort': $('input[name="UrlaubszielNeu"]').val(),
    'land': $('#NeuesUrlaubzieltabelle select[name="land"]').val(),
    'kurzbeschreibung': $('#NeuesUrlaubzieltabelle input[name="Kurzbeschreibung"]').val(),
    'startdatum': $('#NeuesUrlaubzieltabelle input[name="Startdatum"]').val(),
    'enddatum': $('#NeuesUrlaubzieltabelle input[name="Enddatum"]').val(),
    'distanz': $('#NeuesUrlaubzieltabelle input[name="Distanz"]').val(),
    'transportmittel': $('#NeuesUrlaubzieltabelle select[name="Transportmittel"]').val(),
    'kostenrahmen': $('#NeuesUrlaubzieltabelle input[name="Kosten"]').val()
};
    alert(JSON.stringify(formData));
    // Verarbeiten Sie das Formular
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/urlaubsziel',
        data: JSON.stringify(formData),
        success: function(data, textStatus, jQxhr) {
            loadDataTable();
            updateSelect();
        },
        error: function(jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });

    // Verhindern Sie das normale Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();
}

function updateUZ(event) {
alert($('input[name="updateUrlaubszielNeu"]').val());
alert($('input[name="updateStartdatum"]').val());
alert($('select[name="updateland"]').val());

    var id = $('#uzid').val();
    var updatedData = {

        'ort': $('input[name="updateUrlaubszielNeu"]').val(),
        'land': $('#UpdateNeuesUrlaubzieltabelle select[name="updateland"]').val(),
        'kurzbeschreibung': $('#UpdateNeuesUrlaubzieltabelle input[name="updateKurzbeschreibung"]').val(),
        'startdatum': $('#UpdateNeuesUrlaubzieltabelle input[name="updateStartdatum"]').val(),
        'enddatum': $('#UpdateNeuesUrlaubzieltabelle input[name="updateEnddatum"]').val(),
        'distanz': $('#UpdateNeuesUrlaubzieltabelle input[name="updateDistanz"]').val(),
        'transportmittel': $('#UpdateNeuesUrlaubzieltabelle select[name="updateTransportmittel"]').val(),
        'kostenrahmen': $('#UpdateNeuesUrlaubzieltabelle input[name="updateKosten"]').val()
    };
    $.ajax({
      url: '/urlaubsziel/' + id,
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
function deleteUrlaubsvorschlag() {
    alert($('input[name="uzid_del"]').val());
    var id = $('#uzid_del').val();

    $.ajax({
        url: '/urlaubsziel/' + id,
        type: 'DELETE',
        success: function(id) {
          loadDataTable();
          loadSortiertPrio();
          updateSelect();
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.error('Fehler beim Löschen der Instanz mit der ID ' + id + ': ' + errorThrown);
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
            { "data": "ort" },
            { "data": "land" },
            { "data": "kurzbeschreibung" },
            { "data": "startdatum"},
            { "data": "enddatum"},
            { "data": "distanz"},
            { "data": "transportmittel"},
            { "data": "kostenrahmen"}


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

function postVorschlag(event) {

alert($('input[name="vorschlag_pid"]').val());
alert($('#vorschlag_anlegen input[name="vorschlag_uzid"]').val());
alert($('#vorschlag_anlegen input[name="vorschlag_prio"]').val());

    // Holen Sie die Formulardaten
var formData = {
    'person_id': $('#vorschlag_anlegen input[name="vorschlag_pid"]').val(),
    'uz_uzid': $('#vorschlag_anlegen input[name="vorschlag_uzid"]').val(),
    'prio': $('#vorschlag_anlegen input[name="vorschlag_prio"]').val()

};
    alert(JSON.stringify(formData));
    // Verarbeiten Sie das Formular
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/vorschlag',
        data: JSON.stringify(formData),
        success: function(data, textStatus, jQxhr) {
            loadSortiertPrio();
            updateSelect();
        },
        error: function(jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });

    // Verhindern Sie das normale Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();
}


function updateSelect() {
    $.ajax({
    url: "/", // replace with your server-side script URL
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

