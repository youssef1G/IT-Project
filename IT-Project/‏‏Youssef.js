

document.getElementById('loan-form').addEventListener('submit', function(y) {
  y.preventDefault();
  const carPrice = parseFloat(document.getElementById('car-price').value);
  const downPayment = parseFloat(document.getElementById('down-payment').value);
  const loanTerm = parseInt(document.getElementById('loan-term').value);
  const loanAmount = carPrice - downPayment;
  const monthlyPayment = loanAmount / loanTerm;
  document.getElementById('result').textContent = `Estimated Monthly Payment: ${monthlyPayment.toFixed(3)} LE`;
});
