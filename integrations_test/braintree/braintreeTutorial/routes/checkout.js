var express = require('express');
var router = express.Router();
var braintree = require('braintree');

router.post('/', function(req, res, next) {
    var gateway = braintree.connect({
        environment: braintree.Environment.Sandbox,
        merchantId: 'w223v5zd43njjwjp',
        publicKey: 'dvdndmb7d59yvpjk',
        privateKey: '52450b7b9c46ceae0574c6e0d65e2717'
    });

    // Use the payment method nonce here
    var nonceFromTheClient = req.body.paymentMethodNonce;
    // Create a new transaction for $10
    var newTransaction = gateway.transaction.sale({
        amount: '10.00',
        paymentMethodNonce: nonceFromTheClient,
        options: {
            // This option requests the funds from the transaction
            // once it has been authorized successfully
            submitForSettlement: true
        }
    }, function(error, result) {
        if (result) {
            res.send(result);
        } else {
            res.status(500).send(error);
        }
    });
});

module.exports = router;
