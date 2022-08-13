n = function (e, t) {
    for (var a = ("" + e).split("").reverse(), o = ("" + t).split("").reverse(), r = [], n = a.length, i = o.length, l = 0, c = n + i - 1; l <= c; l++) r[l] = 0;
    for (l = 0; l < i; l++)
        for (var s = 0; s < n; s++) r[s + l] += parseInt(a[s], 10) * parseInt(o[l], 10), r[s + 1 + l] += Math.floor(r[s + l] / 10), r[s + l] = r[s + l] % 10;
    return r.reverse(), 0 == r[0] && r.shift(), r.join("")
}
i = function (e, t) {
    for (var a = ("" + e).split("").reverse(), o = ("" + t).split("").reverse(), r = a.length, n = o.length, i = 0, l = 0, c = 0, s = 0, d = 0, u = Math.max(r, n); d < u; d++) l = d < r ? parseInt(a[d], 10) : 0, c = d < n ? parseInt(o[d], 10) : 0, s = Math.round(l) + Math.round(c) + i, a[d] = "" + s % 10, i = s >= 10 ? 1 : 0;
    return 1 == i && a.push("1"), a.reverse().join("")
}
l = function (e) {
    var t = n(e, "18014398509481984"),
        a = n(Math.round(Math.random() * parseInt("4194304", 10)), "4294967296"),
        o = new Date,
        r = 1e3 * (3600 * o.getHours() + 60 * o.getMinutes() + o.getSeconds()) + o.getMilliseconds();
    return i(i(t, a), r)
}
// 获取get_search_id:l(3)
