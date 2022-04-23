from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import time
import math

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message, textsize
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from PIL import ImageFont

from luma.core.sprite_system import framerate_regulator



kofont = ImageFont.truetype("dalmoori.ttf", 8)


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)
virtual = viewport(device, width=1000, height=8)

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"status": "success"}


@app.get("/pixel/{item_id}")
def read_item(item_id: str):
		msg = str(item_id)
		
		
		if len(msg) <= 4:
		    stt = "static"
		    with canvas(device) as draw:
		        w, h = draw.textsize(text=msg, font=kofont)
		        left = (device.width - w) / 2
		        top = (device.height - h) / 2
		        draw.text((left, top), text=msg, fill="white", font=kofont)
		else:
		    stt = "scroll"
		    with canvas(device) as draw:
		        w, h = draw.textsize(text="          "+msg+"          ", font=kofont)
		
		    virtual = viewport(device, width=w, height=8)
		    with canvas(virtual) as draw:
		        w, h = draw.textsize(text="          "+msg, font=kofont)
		        left = (device.width - w) / 2
		        top = (device.height - h) / 2
		        draw.text((left, top), text="          "+msg+"          ", fill="white", font=kofont)
		    for offset in range(int(w-32)):
		        virtual.set_position((offset, 0))
		        time.sleep(0.05)

		time.sleep(0.05)
		return {"text": item_id, "scrollstatus": stt}
