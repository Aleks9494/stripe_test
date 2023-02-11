console.log("Sanity check!");

fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
    var stripe = Stripe(data.publicKey);
    var pk = appConfig.pk;
    console.log(pk);
    console.log(data.publicKey);
    document.querySelector("#submitBtn").addEventListener("click", () => {
        fetch(`/buy/${pk}`)
        .then((result) => { return result.json(); })
        .then((data) => {
        console.log(data);
        return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
        .then((res) => {
        console.log(res);
    });
  });
});