/** @format */

// Toggle Description
function toggleDescription(taskId) {
  const description = document.getElementById(`desc-${taskId}`);
  if (description.classList.contains("hidden")) {
    description.classList.remove("hidden");
  } else {
    description.classList.add("hidden");
  }
}

// Notification Button
$(document).ready(function () {
  $("#notifBtn").on("click", function (event) {
    event.stopPropagation();
    $("#notifDropdown").toggleClass("hidden");
    $("#messageLength").addClass("hidden");
  });

  $(document).on("click", function () {
    $("#notifDropdown").addClass("hidden");
  });

  $("#notifDropdown").on("click", function (event) {
    event.stopPropagation();
  });

  // Profile Dropdown
  $("#profileImage").on("click", function (event) {
    event.stopPropagation();
    $("#dropdownMenu").toggleClass("hidden");
  });

  $(document).on("click", function () {
    $("#dropdownMenu").addClass("hidden");
  });

  $("#dropdownMenu").on("click", function (event) {
    event.stopPropagation();
  });

  $("#appsBtn").on("click", function (event) {
    event.stopPropagation();
    $("#appDropdown").toggleClass("hidden");
  });

  $(document).on("click", function () {
    $("#appDropdown").addClass("hidden");
  });

  $("#addTaskBtn").on("click", function (event) {
    event.stopPropagation();
    $("#addTaskForms").toggleClass("hidden");
  });

  $("#closeForms").on("click", function (event) {
    event.stopPropagation();
    $("#addTaskForms").toggleClass("hidden");
  });

  $("#futureListsBtn").on("click", function () {
    if ($("#futureDropdown").hasClass("hidden")) {
      $("#futureDropdown").removeClass("hidden");
    } else {
      $("#futureDropdown").addClass("hidden");
    }
  });

  $("#futureDropdown").on("click", function (event) {
    event.stopPropagation();
  });

  $(document).on("click", function (event) {
    const target = $(event.target);

    if (!target.closest("#notifBtn, #notifDropdown").length) {
      $("#notifDropdown").addClass("hidden");
    }
    if (!target.closest("#profileImage, #dropdownMenu").length) {
      $("#dropdownMenu").addClass("hidden");
    }
    if (!target.closest("#appsBtn, #appDropdown").length) {
      $("#appDropdown").addClass("hidden");
    }
    if (!target.closest("#editFormBtn, #edit_form").length) {
      $("#edit_form").addClass("hidden");
    }
  });

  // Edit Form Toggle
  const editForm = document.getElementById("edit_form");
  if (editForm) {
    // check if exists
    if (editForm.classList.contains("hidden")) {
      editForm.classList.remove("hidden");
    } else {
      editForm.classList.add("hidden");
    }

    $(document).on("click", function () {
      $("#edit_form").addClass("hidden");
    });

    $("#edit_form").on("click", function (event) {
      event.stopPropagation();
    });
  }
});
