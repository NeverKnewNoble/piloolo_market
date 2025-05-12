// Copyright (c) 2025, carbonitesolutions X Nortex and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Cart", {

// });


// frappe.ui.form.on("ordered Items", {

//     quantity: function (frm, cdt, cdn) {
//         calculate_item_total(cdt, cdn);
//         update_cart_total(frm);
//     },
//     item_price: function (frm, cdt, cdn) {
//         calculate_item_total(cdt, cdn);
//         update_cart_total(frm);
//     },
//     item_total: function (frm) {
//         update_cart_total(frm);
//     },
//     order_items_remove: function (frm) {
//         update_cart_total(frm);
//     }
// });


// function calculate_item_total(cdt, cdn) {
//     let row = locals[cdt][cdn];
//     if (row.quantity && row.item_price) {
//         row.item_total = row.quantity * row.item_price;
//         frappe.model.set_value(cdt, cdn, "item_total", row.item_total);
//     }
// }

// function update_cart_total(frm) {
//     let total = 0;
//     frm.doc.order_items.forEach(row => {
//         if (row.item_total) {
//             total += row.item_total;
//         }
//     });
//     frm.set_value("total", total);
// }




frappe.ui.form.on("Cart", {
    // Optional: Recalculate total on form load (if needed)
    onload(frm) {
        update_cart_total(frm);
    }
});

frappe.ui.form.on("ordered Items", {
    quantity: function (frm, cdt, cdn) {
        calculate_item_total(frm, cdt, cdn);
    },
    item_price: function (frm, cdt, cdn) {
        calculate_item_total(frm, cdt, cdn);
    },
    order_items_add: function (frm, cdt, cdn) {
        calculate_item_total(frm, cdt, cdn);  // New row: trigger calc
        update_cart_total(frm);               // Update total immediately
    },
    order_items_remove: function (frm) {
        update_cart_total(frm);
    }
});


// Calculates item_total and then updates total
function calculate_item_total(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.quantity && row.item_price) {
        row.item_total = row.quantity * row.item_price;
        frappe.model.set_value(cdt, cdn, "item_total", row.item_total);
    } else {
        frappe.model.set_value(cdt, cdn, "item_total", 0);
    }

    // Update the cart total after item total change
    update_cart_total(frm);
}

function update_cart_total(frm) {
    let total = 0;
    frm.doc.order_items.forEach(row => {
        total += row.item_total || 0;
    });

    frm.set_value("total", total);
    frm.refresh_field("total"); 
}