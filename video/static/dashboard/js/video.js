var addVideoForm = $('#add-video-form')
//默认为关闭状态
var openAddVideoBtnStauts = false;
$('#open-add-video-btn').click(function () {
    if (openAddVideoBtnStauts == false){
        addVideoForm.show()
        openAddVideoBtnStauts = true
    }else{
        addVideoForm.hide()
        openAddVideoBtnStauts = false
    }

});