// 브라우저의 기본 동작
const link = document.querySelector("#link");
const checkbox = document.querySelector("#checkbox");
const input = document.querySelector("#input");
const text = document.querySelector("#text");

// event.preventDefault
link.addEventListener("click", function(e) {
  e.preventDefault();
  alert("지금은 이동할 수 없습니다.")
})

input.addEventListener('keydown', function(e) {
  // checked -> boolean 속성 type이 checkbox 또는 radio일 때만 사용 
  if (!checkbox.checked){
    e.preventDefault();
    alert("체크박스를 먼저 클릭해 주세요")
  }
})

// 우클릭 방지 
document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
  alert("마우스 오른쪽 클릭은 사용이 불가능합니다")
})
