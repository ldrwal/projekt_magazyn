$(document).ready(function () {
    $('input,textarea').attr('autocomplete', 'off');

    function fetch_item_list() {
        $.ajax({
            url: $("#data_table").attr("data-url"),
            method: "get",
            success: function (response) {
                $("#data_table").html(response.html);
            }
        })
    }


    fetch_item_list();

    // $(document).on("click", "#btn-delete", function () {
    //     $("#removeItemModal").modal("show");
    // });

    $(document).on("click", "#btn-yes-delete", function () {
        $.ajax({
            url: $("#btn-delete").attr("data-url"),
            type: "delete",
            success: function (response) {
                $("#itemTable").html(response.html);
                $("#removeItemModal").modal("hide");
            }

        })
    })

    // $(document).on("click", "#btn-delete", function () {
    //     $("#removeItemModal").modal("show");
    // });

    $(document).on("click", "#createItemBtn", function () {
        if ($(".create-form").attr("itemName") == '') {
            null
        }
        else {
            $.ajax({
                url: $("#btn-add").attr("data-url"),
                type: "post",
                dataType: "json",
                data: $(".create-form").serialize(),
                success: function (response) {
                    $("#itemTable").html(response.html);
                    $("#removeItemModal").modal("hide");
                }

            })
        }
    })

    $(document).on("click", "#btn-update", function () {
        $.ajax({
            url: $("#btn-update").attr("data-url"),
            type: "get",
            success: function (response) {
                $("#editItemModal .modal-body").html(response.html);
                $("#editItemModal").modal("show");
            }

        })
    })

    $(document).on("click", "#updateItemBtn", function () {
        $.ajax({
            url: $("#updateItemBtn").attr("data-url"),
            type: "post",
            dataType: "json",
            data: $(".update-form").serialize(),
            success: function (response) {
                $("#itemTable").html(response.html);
                $("#editItemModal").modal("hide");
            }

        })
    })
});

