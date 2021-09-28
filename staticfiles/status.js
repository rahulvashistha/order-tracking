function setStatus(status, statusvalue){
    switch(statusvalue){
        case "Order Recieved":
            var orderstatus = document.getElementById('or');
            orderstatus.setAttribute('class', status);
            break;
        case "In Transit":
            var orderstatus = document.getElementById('or');
            orderstatus.setAttribute('class', status);
            var orderstatus = document.getElementById('it');
            orderstatus.setAttribute('class', status);
            break;
        case "Out for Delivery":
            var orderstatus = document.getElementById('or');
            orderstatus.setAttribute('class', status);
            var orderstatus = document.getElementById('it');
            orderstatus.setAttribute('class', status);
            var orderstatus = document.getElementById('ofd');
            orderstatus.setAttribute('class', status);
            break;
        case "Order Delivered":
            var orderstatus = document.getElementById('or');
            orderstatus.setAttribute('class', status);
            var orderstatus = document.getElementById('it');
            orderstatus.setAttribute('class', status);
            var orderstatus = document.getElementById('ofd');
            orderstatus.setAttribute('class', status);
            var orderstatus = document.getElementById('od');
            orderstatus.setAttribute('class', status);
            break;
        default:
            var orderstatus = document.getElementById('or');
            orderstatus.setAttribute('class', status);
        }
    
  }
