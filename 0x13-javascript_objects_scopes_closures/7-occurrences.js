#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const countOccurences = function (list, searchElement) {
    if (list[0] === undefined || list.length === 0) {
      return (0);
    } else {
      if (list[0] === searchElement) {
        return (1 + countOccurences(list.slice(1), searchElement));
      } else {
        return (countOccurences(list.slice(1), searchElement));
      }
    }
  };
  return (countOccurences(list, searchElement));
};
