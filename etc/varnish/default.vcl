# VCL configuration file for Varnish.
# It defines backends for each Plone instance and uses hash load balancing.
#
# This file must me symlinked to /etc/varnish/default.vcl

vcl 4.0;

import directors;
import std;

# probe definition for health checks: 3 of the last 8 tests must succeed

probe healthcheck {
    .interval = 10s;
    .request = "HEAD / HTTP/1.1";
    .timeout = 3s;
}

# backend definitions for Plone instances

backend intance1 {
    .host = "127.0.0.1"; .port = "8081"; .probe = healthcheck;
}

backend intance2 {
    .host = "127.0.0.1"; .port = "8082"; .probe = healthcheck;
}

sub vcl_init {
    new plone = directors.hash();
    plone.add_backend(intance1, 1);
    plone.add_backend(intance2, 1);
}

sub vcl_recv {
    set req.backend_hint = plone.backend(req.url);
    call clean_up_cookies;
}

sub vcl_hit {
    if (obj.ttl >= 0s) {
        return (deliver);
    }

    if (!std.healthy(req.backend_hint) && (obj.ttl + obj.grace > 0s)) {
        return (deliver);
    }

    return (fetch);
}

sub vcl_backend_response {
    set beresp.grace = 1h;
}

# Clean up all cookies except for the ones we must care
# https://www.varnish-cache.org/docs/4.0/users-guide/increasing-your-hitrate.html#cookies
# http://docs.plone.org/develop/plone/sessions/cookies.html
sub clean_up_cookies {
    if (req.http.Cookie) {
        set req.http.Cookie = ";" + req.http.Cookie;
        set req.http.Cookie = regsuball(req.http.Cookie, "; +", ";");
        set req.http.Cookie = regsuball(req.http.Cookie, ";(__ac|__cp|_ZopeId|statusmessages)=", "; \1=");
        set req.http.Cookie = regsuball(req.http.Cookie, ";[^ ][^;]*", "");
        set req.http.Cookie = regsuball(req.http.Cookie, "^[; ]+|[; ]+$", "");

        if (req.http.Cookie == "") {
            unset req.http.Cookie;
        }
    }
}
