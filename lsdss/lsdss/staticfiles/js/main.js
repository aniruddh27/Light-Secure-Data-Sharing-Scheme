$('.carousel').carousel()

// tooltip
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

// Register new data

document.getElementById('registerData').addEventListener('click',function(){
    
    document.getElementById("registerForm").submit();

})


// encrypt file
// document.getElementById('encryptFile{{file.id}}').addEventListener('click',function(){
//     print('cclcike')
//     setInterval(function(){
//         window.location.reload();
//     },2000)
// })
 

// key generation

document.getElementById("requestKeyBtn").addEventListener('click',changeButton)

function changeButton() {
    document.getElementById("requestKeyForm").submit();
    console.log("clicked")
    status="{{status}}"
    console.log(status)
    if (status="Key Requested") {
        document.getElementById("requestKeyBtn").setAttribute("value","Done");
        document.getElementById("requestKeyBtn").disabled=true;
        document.getElementById("requestKeyBtn").classList.remove("btn", "btn-primary")
        document.getElementById("requestKeyBtn").classList.add("btn", "btn-success")
    }
}
document.getElementById("generateKeyBtn").addEventListener('click',generateKey)
document.getElementById("sendKeyBtn").addEventListener('click',sendKey)
function generateKey(){
    window.location.reload();
}

function sendKey(){
    setInterval(function(){
        document.getElementById("sendKeyBtn").setAttribute("value","Key Sent");
        document.getElementById("sendKeyBtn").classList.remove("btn", "btn-primary")
        document.getElementById("sendKeyBtn").classList.add("btn", "btn-success")
    },2000)
        document.getElementById("sendKeyBtn").setAttribute("value","Sending...");
}


//upload file into system
document.getElementById("uploadFileBtn").addEventListener('click',uploadFileintoSystem)

function uploadFileintoSystem(){
    setInterval(function(){
        document.getElementById("uploadFileBtn").setAttribute("value","File Uploaded");
        document.getElementById("uploadFileBtn").classList.remove("btn", "btn-primary")
        document.getElementById("uploadFileBtn").classList.add("btn", "btn-success")
        window.location.reload();
    },2000)
        document.getElementById("uploadFileBtn").setAttribute("value","Uploading...");
    
}

// reload cloud file upload page
const cpr="{{onCloudPage}}"
console.log(cpr)
alert(cpr)
if (cpr){
    window.location.reload();
    cpr=false;
}

// Add file Attributes Cloud Attributes
// document.getElementById("addAttributesBtn").addEventListener('click',addFileAttributes)

// function addFileAttributes(){
//     if(fileAttributes==null || fileAttributes==""){
//         alert("Need atleast 1 attribute")
//     }
// }

// let x= document.getElementsByTagName("button")
//     for (let i = 0; i < x.length; i++) {
//         const element = x[i];
//         element.addEventListener("click",function(element){
//         if(x[i].id == "registerButton"){
//             // showForm(x[i].id)
//             $('#registerModal').modal({backdrop: 'static', keyboard: false})
//         }
//         else if(x[i].id == "loginButton") {
//             // showForm(x[i].id)
//             $('#loginModal').modal({backdrop: 'static', keyboard: false})
//         }
//     })
//     }
// function showForm(formType) {
//     // $('#registerModal').modal({backdrop: 'static', keyboard: false})
//     console.log(formType)
//     if(formType=="registerButton"){
//         $('#registerModal').modal({backdrop: 'static', keyboard: false})
//         console.log(document.getElementById('registerForm'))
//         document.getElementById('registerForm').style.display="block"
//         // $('#registerModal').modal('hide')

//     }
//     else{
//         console.log(document.getElementById('loginForm'))
//         $('#loginModal').modal({backdrop: 'static', keyboard: false})
//         document.getElementById('registerForm').style.display="none"
//         document.getElementById('loginForm').style.display="block"
//         // $('#registerModal').modal('hide')
//     }
// }   


// document.getElementById('registerForm').style.display="none";
// document.querySelector('.homeBtn').style.display="none";

// function goHome() {
//     document.getElementById('registerForm').style.display="none";
//     document.querySelector('.homeBtn').style.display="none";
//     document.querySelector('.homeBtn1').style.display="block";
//     document.querySelector('.homeBtn2').style.display="block";
// }

// function showRegister() {
//     document.getElementById('registerForm').style.display="block";
//     document.querySelector('.homeBtn').style.display="block";
//     document.querySelector(".homeBtn1").style.display="none";
//     document.querySelector(".homeBtn2").style.display="none";
// }

// function login() {
//     document.getElementById('registerForm').style.display="block";
//     document.querySelector(".homeBtn").style.display="block";
//     document.querySelector('.homeBtn1').style.display="none";
//     document.querySelector('.homeBtn2').style.display="none";
// }
