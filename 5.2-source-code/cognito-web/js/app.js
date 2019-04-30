var CognitoData = {
  UserPoolId: '{YOUR_COGONITO_POOL_ID}',
  ClientId: '{YOUR_COGONITO_APP_CLIENT_ID}'
}
window.CognitoData = CognitoData

function $id (id) {
  return document.getElementById(id)
}
function showOK (msg) {
  document.getElementById('info').className = 'ok'
  document.getElementById('info').innerHTML = msg
}
function showErr (err) {
  document.getElementById('info').className = 'ok'
  document.getElementById('info').innerHTML = err
}
