const fileInput = document.getElementById('fileInput')
const fileText = document.getElementById('fileText')

fileInput.addEventListener('change', function(event){
    console.log(this)
    console.log(this.files)
    file = this.files[0]
    fileText.textContent = file.name
})