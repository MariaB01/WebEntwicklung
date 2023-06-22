$(document).ready(function() {
    loadDataTable(); //Funktion zum Laden der Urlaubszieldaten in eine Tabelle
    loadPersonDataTable(); //Funktion zum Laden der Personendaten in eine Tabelle
    loadSortiertPrio(); //Funktion zum Laden der sortierten Prioritätsdaten in eine Tabelle
    updateSelect();
    // Verarbeite das Formular "postUZ" beim Klicken auf den Button "#newUZButton"
    $("#newUZButton").click(function(event) {
        postUZ(event);
    })
    // Verarbeite das Formular "updateUZ" beim Klicken auf den Button "#updateUZ"
    $('#updateUZ').click(function(event) {
        updateUZ(event);
    });
    // Verarbeite das Formular "deleteUrlaubsvorschlag" beim Klicken auf den Button "#deleteUz"
  $('#deleteUZ').click(function(event) {
      deleteUrlaubsvorschlag();
    });
  // Verarbeite das Formular "postVorschlag" beim Absenden des Formulars
  $("#vorschlag_anlegen").submit(function(event) {
      postVorschlag(event);
    });
      // Verarbeite das Formular "postPerson" beim Klicken auf den Button "#Benutzer_neu"
  $('#Benutzer_neu').click(function() {
        postPerson();
    });
  // Verarbeite das Formular "updatePerson" beim Klicken auf den Button "#Benutzer_upd"
  $('#Benutzer_upd').click(function() {
        updatePerson();
    });
  // Verarbeite das Formular "deletePerson" beim Klicken auf den Button "#Benutzer_upd"
     $('#Benutzer_del').click(function() {
        deletePerson();
    });

});
// Funktion zum Hinzufügen einer neuen Urlaubsziel-Instanz
function postUZ(event) {
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
// Funktion zum Updaten einer Urlaubsziel-Instanz
function updateUZ(event) {
    // Holen Sie die Formulardaten
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
        // Verarbeiten Sie das Formular
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
// Funktion zum Löschen einer Urlaubsziel-Instanz

function deleteUrlaubsvorschlag(event) {
    // Holen Sie die Formulardaten
    var id = $('#uzid').val();
        // Verarbeiten Sie das Formular
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

// Funktion zum Laden der Urlaubszieltabelle
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

// Funktion zum Laden der Personentabelle
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
// Funktion zum Laden der Gesamtprioritätenltabelle
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



        ],
        "order": [[1, "desc"]] // Sortiere nach dem zweiten Spaltenindex (prio) absteigend
    });
}
// Funktion zum Hinzufügen einer neuen Priorität
function postVorschlag(event) {
    // Holen Sie die Formulardaten
var formData = {
    'person_id': $('#vorschlag_anlegen input[name="vorschlag_pid"]').val(),
    'uz_uzid': $('#vorschlag_anlegen input[name="vorschlag_uzid"]').val(),
    'prio': $('#vorschlag_anlegen input[name="vorschlag_prio"]').val()
};
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

// Funktion zum Hinzufügen einer neuen PersonenInstanz

function postPerson(event) {
    // Holen Sie die Formulardaten
var formData = {
    'name': $('input[name="pname"]').val()
    };
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
        }
    });

    // Verhindern Sie das normale Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();
}

// Funktion zum Updaten einer neuen PersonenInstanz

function updatePerson(event) {

var id = $('#pid').val();
    // Holen Sie die Formulardaten
var formData = {
    'pid': $('input[name="pid"]').val(),
    'name': $('input[name="pname"]').val()
    };
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
        }
    });
    // Verhindern Sie das normale Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();
}

// Funktion zum Löschen einer neuen PersonenInstanz

function deletePerson(event) {

    // Holen Sie die Formulardaten
var id = $('#pid').val();
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

