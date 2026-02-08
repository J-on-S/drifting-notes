//assume database is complete!
const response = fetch('../api/receive/anon-user-placeholder')
fetch('../api/receive/anon-user/placeholder').then(res => res.json()).then(data => console.log(data))