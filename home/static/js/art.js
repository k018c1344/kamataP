//リスト要素を取得する
const list = document.querySelector(".list");
//リスト要素の子要素（li）をすべて取得する
const listChildren = list.children;

//listChildrenの数だけ繰り返し処理を実行する
for (let item of listChildren) {
    item.addEventListener(
        "mouseover",
        function () {
            let target = item.dataset.target;
            let el = document.getElementById("project");
            el.classList = "";
            el.classList.add(target);
        },
        false
    );
}