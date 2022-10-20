# Leveldesign

Jede Strecke muss linear sein, damit die Spieler nahe beeinander bleiben.

## Motionsickness

"Als Motion Sickness bezeichnet man ein Zustand, in dem eine Unstimmigkeit zwischen visuell wahrgenommener Bewegung und dem Bewegungssinn des Gleichgewichtssystems besteht." - Google

# Streckendesigns

## Iteration 1 - Spirale

Die Spieler fährt in einer Spirale um den VR-Spieler herum. Der VR-Spieler muss sich hier permanent im Kreis drehen um mit den PC-Spielern mitzukommen.

## Iteration 2 - Crystalball - Gerade/Gecullte Strecke

Die Spieler fahren an einer geraden Strecke entlang. Sie müssen hier nicht so viel im Kreis lenken und können sich mehr auf die Strecke und die vom VR-Spieler platzierten Obstacles konzentrieren. Allerdings ist dieses Design vom Leveldesign her sehr eingeschränkt. 

Auch bringt es einige Probleme auf der VR-Seite mit sich. Da die Strecke sehr lange in eine Richtung gestreckt ist, muss sich der VR-Spieler permanent mit den anderen mitbewegen oder die Strecke muss "gecullt" und bewegt werden. Leveldesign mit einer "gecullten" Strecke ist wieder sehr eingeschränkt da der VR-Spieler nie die Möglichkeit hat vorrauszuplanen und das Spiel auch für den VR-Spieler sehr "reaktiv" wird.

## Iteration 3 - Berg

### PC - Berg-Strecke

Spieler fahren auf einem Berg. Auf dem Berg kann die Strecke in Kurven und längeren "geraderen" Strecken verlaufen. Das Level-Design ist sehr frei bei dieser Art von Strecke. Das VR-Spieler müsste sich allerdings permanent um den Berg herumbewegen

### VR - Schallplatte

Die Spielfläche in VR ist in den meisten fällten, vorallem Zuhause, sehr begrenzt. Es muss auch für Personen die nicht sehr viel Platz haben möglich sein, den ganzen Berg zu umrunden. Das Rotieren des Berges macht technische Probleme, daher können wir ihn nicht rotieren. Der Spieler darf allerdings nie das Gefühl haben, dass wir ihn bewegen.

Um das möglich zu machem, haben wir die "Schallplatte" erfunden. Sie macht es möglich einfach mit den verscheidenen Stellen der Strecke und den Objekten in dem VR-Space zu interagieren, ohne dass "Motionsickness" zu einem größeren Problem wird, da der VR-Spieler das gefühl hat als würde sich der Berg rotieren.

Um dem VR-Spieler aber trodzdem nicht in der Auswahl seiner Spells beschränken zu müssen, muss man die Maschienen in zwei Bereichen aufteilen. Zwischen diesen Bereichen kann der VR-Spieler wechseln indem er einen Knopf drückt. Dadurch können wir dem VR-Spieler mehr Spells zugänglich machen, ohne dass wir ihn bewegen müssen.

#### Verschiebbare Obstacles

Um den Spielern etwas mehr diversität auf einer einzigen Strecke bieten zu können, kann der VR-Spieler bereiche der Strecke aus und einschalten. Das kann aufgrund der Reaktionszeit der PC-Spieler allerdings nur dann möglich sein, wenn die spieler noch weit genug davon entfernt sein. Damit die Strecke Lienear bleibt, kann der VR-Spieler den Verlauf der Strecke nur verändern, indem er Blockaden der Strecken verschiebt.

### Schluchten

Der VR-Spieler hat die Möglichkeit Wege einstürzen zu lassen. Die eingestürtzten Teile dürfen nicht größer als einen Sprung sein damit die Spieler noch eine Chance haben.

Diese Wege stürtzen auch nicht sofort ein. Sie haben eine Animation, die die Spieler darauf vorbereitet, damit sie noch reagieren können.

## Kurven vs. Geraden

Die PC-Spieler werden so umgesetzt, dass sie grundsätzlich von alleine bergab fahren können. Eine permanente links kurve bedeutet also nicht, dass der PC-Spieler permanent nach links lenken muss. Jedoch wird es mit der Zeit sehr langweilig die Ganze zeit in eine Richtung fahren zu müssen. Daher wird die Map aus vielen Kurven bestehen, die Ecken und Kanten davon bieten gute Möglichkeiten Long-Term-Spells zu plazieren da sie da die grrößte fäche abdecken.

## Quick Topdown View

<img title="" src="sketches/strecke_topdown.png" alt="Kiku" width="241">
