from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

pdf = PDF()
pdf.add_page()


# specify font
pdf.set_font('helvetica', '', 16)

pdf.cell(0,0, 'A cell with some words')

pdf.write_html("""
    <table  width = 50%>
      <thead>
        <tr>
          <th align="left" width="30%">ID</th>
          <th align="left" width="70%">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Alice</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Bob</td>
        </tr>
      </tbody>
    </table>
  </section>
""")

pdf.output("pdf_table.pdf")
