from ninja import NinjaAPI
api = NinjaAPI(title="Prometheus Testing")
@api.get("/hello")
def hello(request):
    return {"message": "hello"}
