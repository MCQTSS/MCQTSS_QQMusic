window = global;
location = {"host": "y.qq.com"}
global.navigator = {userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"};
var ventor = require('./ventor.js')
!function (e) {
    function t(t) {
        for (var r, n, f = t[0], c = t[1], i = t[2], l = 0, u = []; l < f.length; l++) n = f[l], Object.prototype.hasOwnProperty.call(o, n) && o[n] && u.push(o[n][0]), o[n] = 0;
        for (r in c) Object.prototype.hasOwnProperty.call(c, r) && (e[r] = c[r]);
        for (b && b(t); u.length;) u.shift()();
        return d.push.apply(d, i || []), a()
    }

    function a() {
        for (var e, t = 0; t < d.length; t++) {
            for (var a = d[t], r = !0, n = 1; n < a.length; n++) {
                var c = a[n];
                0 !== o[c] && (r = !1)
            }
            r && (d.splice(t--, 1), e = f(f.s = a[0]))
        }
        return e
    }

    var r = {}, n = {21: 0}, o = {21: 0}, d = [];

    function f(t) {
        if (r[t]) return r[t].exports;
        var a = r[t] = {i: t, l: !1, exports: {}};
        return e[t].call(a.exports, a, a.exports, f), a.l = !0, a.exports
    }

    f.e = function (e) {
        var t = [];
        n[e] ? t.push(n[e]) : 0 !== n[e] && {
            1: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            20: 1,
            22: 1,
            23: 1,
            24: 1,
            25: 1,
            26: 1
        }[e] && t.push(n[e] = new Promise((function (t, a) {
            for (var r = "css/" + ({
                1: "common",
                3: "album",
                4: "albumDetail",
                5: "album_mall",
                6: "category",
                7: "cmtpage",
                8: "download_detail",
                9: "index",
                10: "msg_center",
                11: "mv",
                12: "mvList",
                13: "mv_toplist",
                14: "notfound",
                15: "player",
                16: "player_radio",
                17: "playlist",
                18: "playlist_edit",
                19: "profile",
                20: "radio",
                22: "search",
                23: "singer",
                24: "singer_list",
                25: "songDetail",
                26: "toplist"
            }[e] || e) + "." + {
                1: "2e3d715e72682303d35b",
                3: "5cf0d69eaf29bcab23d2",
                4: "798353db5b0eb05d5358",
                5: "df4c243f917604263e58",
                6: "20d532d798099a44bc88",
                7: "e3bedf2b5810f8db0684",
                8: "e3bedf2b5810f8db0684",
                9: "ea0adb959fef9011fc25",
                10: "020422608fe8bfb1719a",
                11: "8bdb1df6c5436b790baa",
                12: "47ce9300786df1b70584",
                13: "4aee33230ba2d6b81dce",
                14: "e6f63b0cf57dd029fbd6",
                15: "1d2dbefbea113438324a",
                16: "d893492de07ce97d8048",
                17: "9484fde660fe93d9f9f0",
                18: "67fb85e7f96455763c83",
                19: "5e8c651e74b13244f7cf",
                20: "3befd83c10b19893ec66",
                22: "b2d11f89ea6a512a2302",
                23: "c7a38353c5f4ebb47491",
                24: "df0961952a2d3f022894",
                25: "4c080567e394fd45608b",
                26: "8edb142553f97482e00f"
            }[e] + ".chunk.css?max_age=2592000", o = f.p + r, d = document.getElementsByTagName("link"), c = 0; c < d.length; c++) {
                var i = (b = d[c]).getAttribute("data-href") || b.getAttribute("href");
                if ("stylesheet" === b.rel && (i === r || i === o)) return t()
            }
            var l = document.getElementsByTagName("style");
            for (c = 0; c < l.length; c++) {
                var b;
                if ((i = (b = l[c]).getAttribute("data-href")) === r || i === o) return t()
            }
            var u = document.createElement("link");
            u.rel = "stylesheet", u.type = "text/css", u.onload = t, u.onerror = function (t) {
                var r = t && t.target && t.target.src || o,
                    d = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                d.code = "CSS_CHUNK_LOAD_FAILED", d.request = r, delete n[e], u.parentNode.removeChild(u), a(d)
            }, u.href = o, 0 !== u.href.indexOf(window.location.origin + "/") && (u.crossOrigin = "anonymous"), document.getElementsByTagName("head")[0].appendChild(u)
        })).then((function () {
            n[e] = 0
        })));
        var a = o[e];
        if (0 !== a) if (a) t.push(a[2]); else {
            var r = new Promise((function (t, r) {
                a = o[e] = [t, r]
            }));
            t.push(a[2] = r);
            var d, c = document.createElement("script");
            c.charset = "utf-8", c.timeout = 120, f.nc && c.setAttribute("nonce", f.nc), c.src = function (e) {
                return f.p + "js/" + ({
                    1: "common",
                    3: "album",
                    4: "albumDetail",
                    5: "album_mall",
                    6: "category",
                    7: "cmtpage",
                    8: "download_detail",
                    9: "index",
                    10: "msg_center",
                    11: "mv",
                    12: "mvList",
                    13: "mv_toplist",
                    14: "notfound",
                    15: "player",
                    16: "player_radio",
                    17: "playlist",
                    18: "playlist_edit",
                    19: "profile",
                    20: "radio",
                    22: "search",
                    23: "singer",
                    24: "singer_list",
                    25: "songDetail",
                    26: "toplist"
                }[e] || e) + ".chunk." + {
                    1: "0b15a31f7bc269ea76ff",
                    3: "b3395a2d475262b98fa7",
                    4: "dea94b21a47cdb6d0f65",
                    5: "f5b6937e84f33133b31d",
                    6: "6c4ac3718d0230ac3b1c",
                    7: "ae411fac801093307ebc",
                    8: "f1c40f6b3a431ca4c9ac",
                    9: "52f2369df6a4a3649011",
                    10: "90aef56793aff533bf57",
                    11: "4c23320d028878580c26",
                    12: "b43316a48154164d557b",
                    13: "8adf08693025ab48224f",
                    14: "89eb6da604ebcf2dda2d",
                    15: "c6c19b148a1694a28cbe",
                    16: "0df54200ddf5f7710d42",
                    17: "6838a647ca4abb619832",
                    18: "9d2cbd13db3328dcd357",
                    19: "ce6940fdeda857506a27",
                    20: "8af74f665077243ecefa",
                    22: "5a013d73a1da88cc221e",
                    23: "469f622f5dffdeee26eb",
                    24: "9df420e7d63b8d867fd2",
                    25: "9bea17905ada32dde9b5",
                    26: "bcb481bd9dd2001370ac"
                }[e] + ".js?max_age=2592000"
            }(e), 0 !== c.src.indexOf(window.location.origin + "/") && (c.crossOrigin = "anonymous");
            var i = new Error;
            d = function (t) {
                c.onerror = c.onload = null, clearTimeout(l);
                var a = o[e];
                if (0 !== a) {
                    if (a) {
                        var r = t && ("load" === t.type ? "missing" : t.type), n = t && t.target && t.target.src;
                        i.message = "Loading chunk " + e + " failed.\n(" + r + ": " + n + ")", i.name = "ChunkLoadError", i.type = r, i.request = n, a[1](i)
                    }
                    o[e] = void 0
                }
            };
            var l = setTimeout((function () {
                d({type: "timeout", target: c})
            }), 12e4);
            c.onerror = c.onload = d, document.head.appendChild(c)
        }
        return Promise.all(t)
    }, f.m = e, f.c = r, f.d = function (e, t, a) {
        f.o(e, t) || Object.defineProperty(e, t, {enumerable: !0, get: a})
    }, f.r = function (e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {value: "Module"}), Object.defineProperty(e, "__esModule", {value: !0})
    }, f.t = function (e, t) {
        if (1 & t && (e = f(e)), 8 & t) return e;
        if (4 & t && "object" === typeof e && e && e.__esModule) return e;
        var a = Object.create(null);
        if (f.r(a), Object.defineProperty(a, "default", {
            enumerable: !0,
            value: e
        }), 2 & t && "string" != typeof e) for (var r in e) f.d(a, r, function (t) {
            return e[t]
        }.bind(null, r));
        return a
    }, f.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e.default
        } : function () {
            return e
        };
        return f.d(t, "a", t), t
    }, f.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, f.p = "/ryqq/", f.oe = function (e) {
        throw e
    };
    var c = window.webpackJsonp = window.webpackJsonp || [], i = c.push.bind(c);
    c.push = t, c = c.slice();
    for (var l = 0; l < c.length; l++) t(c[l]);
    var b = i;
    a()
    ventor = f;
}([]);
var o = ventor(350).default;