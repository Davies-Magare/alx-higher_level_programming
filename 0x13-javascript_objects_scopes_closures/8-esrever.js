#!/usr/bin/node
exports.esrever = function (list) {
  function revList (list) {
    if (list.length === 0) {
      return ([]);
    }
    return (revList(list.slice(1)).concat(list[0]));
  }
  return revList(list);
};
