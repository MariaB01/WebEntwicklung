//On Page load - register listeners and load existing videos in datatable
$(document).ready(function() {
    loadDataTable();
    loadPersonDataTable();
    loadSortiertPrio();
    updateSelect();
    //process the form newVideo
    $("#newUZButton").click(function(event) {
        alert('anlegen');
        postUZ(event);
    })

    $('#updateUZ').click(function(event) {
        alert('update');
        updateUZ(event);
    });

  $('#deleteUZ').click(function(event) {
      alert('löschen');
      deleteUrlaubsvorschlag();
    });


  $("#vorschlag_anlegen").submit(function(event) {
      alert('vor Click');
      postVorschlag(event);
    });
  $('#Benutzer_neu').click(function() {
        postPerson();
    });

  $('#Benutzer_upd').click(function() {
        alert("geht");
        updatePerson();
    });

     $('#Benutzer_del').click(function() {
        alert("geht");
        deletePerson();
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
    'land': $('select[name="land"]').val(),
    'kurzbeschreibung': $(' input[name="Kurzbeschreibung"]').val(),
    'startdatum': $('input[name="Startdatum"]').val(),
    'enddatum': $(' input[name="Enddatum"]').val(),
    'distanz': $(' input[name="Distanz"]').val(),
    'transportmittel': $(' select[name="Transportmittel"]').val(),
    'kostenrahmen': $(' input[name="Kosten"]').val()
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
alert($('input[name="UrlaubszielNeu"]').val());
alert($('input[name="Startdatum"]').val());
alert($('select[name="land"]').val());

    var id = $('#uzid').val();
    var updatedData = {

        'ort': $('input[name="UrlaubszielNeu"]').val(),
        'land': $(' select[name="land"]').val(),
        'kurzbeschreibung': $('input[name="Kurzbeschreibung"]').val(),
        'startdatum': $(' input[name="Startdatum"]').val(),
        'enddatum': $(' input[name="Enddatum"]').val(),
        'distanz': $('input[name="Distanz"]').val(),
        'transportmittel': $('select[name="Transportmittel"]').val(),
        'kostenrahmen': $(' input[name="Kosten"]').val()
    };
    $.ajax({
      url: '/urlaubsziel/' + id,
      type: 'PUT',
      contentType: 'application/json',
      data: JSON.stringify(updatedData),
      success: function(data,textStatus, jQxhr) {
        loadDataTable();
        updateSelect();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error updating entry with ID ${id}: ${errorThrown}');
      }
    });

}
function deleteUrlaubsvorschlag(event) {
    alert($('input[name="uzid"]').val());
    var id = $('#uzid').val();

    $.ajax({
        type: 'DELETE',
        contentType: 'application/json',
        url: '/urlaubsziel/'+id,
        data: JSON.stringify(),
        success: function(data, textStatus, jQxhr) {
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
    var table = $('#PersonDataTable').DataTable({
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

function postPerson(event) {

alert($('input[name="pname"]').val());
//alert($('#personen_pflege_tabelle input[name="pid"]').val());

    // Holen Sie die Formulardaten
var formData = {
    'name': $('input[name="pname"]').val()

    };
    alert(JSON.stringify(formData));
    // Verarbeiten Sie das Formular
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/person',
        data: JSON.stringify(formData),
        success: function(data, textStatus, jQxhr) {
            loadPersonDataTable();
            updateSelect();
        },
        error: function(jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
            alert("Fehler");
        }
    });

    // Verhindern Sie das normale Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();
}


function updatePerson(event) {

alert($('input[name="pname"]').val());
//alert($('#personen_pflege_tabelle input[name="pid"]').val());
var id = $('#pid').val();
    // Holen Sie die Formulardaten
var formData = {
    'pid': $('input[name="pid"]').val(),
    'name': $('input[name="pname"]').val()

    };
    alert(JSON.stringify(formData));
    // Verarbeiten Sie das Formular
    $.ajax({
        type: 'PUT',
        contentType: 'application/json',
        url: '/person/'+id,
        data: JSON.stringify(formData),
        success: function(data, textStatus, jQxhr) {
            loadPersonDataTable();
            updateSelect();
        },
        error: function(jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
            alert("Fehler");
        }
    });

    // Verhindern Sie das normale Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();
}


function deletePerson(event) {

alert($('input[name="pid"]').val());
//alert($('#personen_pflege_tabelle input[name="pid"]').val());
var id = $('#pid').val();
    // Holen Sie die Formulardaten

    alert(JSON.stringify());
    // Verarbeiten Sie das Formular
    $.ajax({
        type: 'DELETE',
        contentType: 'application/json',
        url: '/person/'+id,
        data: JSON.stringify(),
        success: function(data, textStatus, jQxhr) {
            loadPersonDataTable();
            updateSelect();
        },
        error: function(jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
            alert("Fehler");
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

