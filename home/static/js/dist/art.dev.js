"use strict";

//リスト要素を取得する
var list = document.querySelector(".list"); //リスト要素の子要素（li）をすべて取得する

var listChildren = list.children; //listChildrenの数だけ繰り返し処理を実行する

var _iteratorNormalCompletion = true;
var _didIteratorError = false;
var _iteratorError = undefined;

try {
  var _loop = function _loop() {
    var item = _step.value;
    item.addEventListener("mouseover", function () {
      var target = item.dataset.target;
      var el = document.getElementById("project");
      el.classList = "";
      el.classList.add(target);
    }, false);
  };

  for (var _iterator = listChildren[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
    _loop();
  }
} catch (err) {
  _didIteratorError = true;
  _iteratorError = err;
} finally {
  try {
    if (!_iteratorNormalCompletion && _iterator["return"] != null) {
      _iterator["return"]();
    }
  } finally {
    if (_didIteratorError) {
      throw _iteratorError;
    }
  }
}