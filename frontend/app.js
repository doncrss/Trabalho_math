const money = new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL',
});

const tabs = document.querySelectorAll('.tab');
const panels = document.querySelectorAll('.panel');

for (const tab of tabs) {
  tab.addEventListener('click', () => {
    const targetId = tab.dataset.target;
    for (const item of tabs) item.classList.toggle('is-active', item === tab);
    for (const panel of panels) {
      const active = panel.id === targetId;
      panel.classList.toggle('is-active', active);
      panel.hidden = !active;
    }
  });
}

function setLoading(form, loading) {
  const button = form.querySelector('.submit-button');
  button.disabled = loading;
  button.firstChild.textContent = loading ? 'Calculando...' : button.dataset.label;
}

function configureButtons() {
  for (const button of document.querySelectorAll('.submit-button')) {
    button.dataset.label = button.firstChild.textContent;
  }
}

function showError(feedback, result, message) {
  feedback.textContent = message;
  result.hidden = true;
}

async function request(endpoint, payload) {
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.detail || 'Não foi possível concluir o cálculo.');
  return data;
}

function numberFrom(form, field) {
  return Number(new FormData(form).get(field));
}

document.querySelector('#desconto-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const feedback = document.querySelector('#desconto-feedback');
  const result = document.querySelector('#desconto-result');
  feedback.textContent = '';
  if (!form.reportValidity()) return;

  setLoading(form, true);
  try {
    const data = await request('/desconto', {
      valor_compra: numberFrom(form, 'valor_compra'),
      cupom: new FormData(form).get('cupom'),
    });
    document.querySelector('#valor-final').textContent = money.format(data.valor_final);
    document.querySelector('#desconto-resumo').textContent = data.desconto_aplicado
      ? 'Cupom aplicado com sucesso'
      : 'Cupom não aplicado';
    document.querySelector('#valor-desconto').textContent = data.desconto_aplicado
      ? `-${money.format(data.valor_desconto)}`
      : 'Sem desconto';
    result.hidden = false;
  } catch (error) {
    showError(feedback, result, error.message);
  } finally {
    setLoading(form, false);
  }
});

document.querySelector('#economia-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const feedback = document.querySelector('#economia-feedback');
  const result = document.querySelector('#economia-result');
  feedback.textContent = '';
  if (!form.reportValidity()) return;

  setLoading(form, true);
  try {
    const data = await request('/economia', {
      renda_mensal: numberFrom(form, 'renda_mensal'),
      gastos_fixos: numberFrom(form, 'gastos_fixos'),
      meta_financeira: numberFrom(form, 'meta_financeira'),
    });
    document.querySelector('#meses-necessarios').textContent = data.possivel_atingir_meta
      ? `${data.meses_necessarios} ${data.meses_necessarios === 1 ? 'mês' : 'meses'}`
      : 'Meta inviável';
    document.querySelector('#economia-resumo').textContent = data.possivel_atingir_meta
      ? 'Com a economia mensal atual'
      : 'Ajuste sua renda ou seus gastos';
    document.querySelector('#economia-mensal').textContent = money.format(data.economia_mensal) + '/mês';
    result.hidden = false;
  } catch (error) {
    showError(feedback, result, error.message);
  } finally {
    setLoading(form, false);
  }
});

configureButtons();
